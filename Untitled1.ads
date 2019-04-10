
#include <stdio.h>          /* for printf() and fprintf() */
#include <sys/socket.h>     /* for socket(), connect(), send(), and recv() */
#include <stdlib.h>         /* for atoi() and exit() */
#include <string.h>         /* for memset() */
#include <unistd.h>         /* for close() */
#include <sys/types.h>
#include <netinet/in.h>
#include <mysql.h>
#include <string.h>
#include "MQTTClient.h"
#define ADDRESS     "m16.cloudmqtt.com:15843"
#define CLIENTID    "ExampleClientPub"
#define TOPIC       "projects"
#define QOS         1
#define TIMEOUT     10000L

#define MAXPENDING 5
#define BUFFSIZE 256
#define PORT 8888

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

void finish_with_error(MYSQL *con)
{
  fprintf(stderr, "%s\n", mysql_error(con));
  mysql_close(con);
  exit(1);
}


int main(int argc, char *argv[])
{

    MYSQL *con = mysql_init(NULL);
    if (con == NULL)
        {
            fprintf(stderr, "mysql_init() failed\n");
            exit(1);
        }
    if (mysql_real_connect(con, "localhost", "usernho", "nho123",
          "testdb", 0, NULL, 0) == NULL)
        {
            finish_with_error(con);
        }

    int servSock, clntSock, n;
    socklen_t clntLen;
    char buffer[BUFFSIZE];
    struct sockaddr_in serv_addr, cli_addr;

    // Create socket for incoming connections
    if ((servSock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)) < 0)
        error("ERROR opening socket");

    // Construct local address structure
    memset(&serv_addr, 0, sizeof(serv_addr));       /* Zero out structure */
    serv_addr.sin_family = AF_INET;                /* Internet address family */
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY); /* Any incoming interface */
    serv_addr.sin_port = htons(PORT);              /* Local port */

    // Bind to the local address
    if (bind(servSock, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("ERROR on binding");

    // Mark the socket so it will listen for incoming connections
    if (listen(servSock, MAXPENDING) < 0)
        error("ERROR on binding");

    // Set the size of the in-out parameter
    clntLen = sizeof(cli_addr);

    // Wait for a client to connect
    if ((clntSock = accept(servSock, (struct sockaddr *) &cli_addr, &clntLen)) < 0)
        error("accept() failed");

    bzero(buffer,BUFFSIZE);

    //start mqtt publish to cloud
    // char PAYLOAD[10];
    MQTTClient client;
    MQTTClient_connectOptions conn_opts = MQTTClient_connectOptions_initializer;
    MQTTClient_message pubmsg = MQTTClient_message_initializer;
    MQTTClient_deliveryToken token;
    int rc;

    MQTTClient_create(&client, ADDRESS, CLIENTID, MQTTCLIENT_PERSISTENCE_NONE, NULL);
    conn_opts.keepAliveInterval = 20;
    conn_opts.cleansession = 1;
    conn_opts.username = "fuwcgyvb";
    conn_opts.password = "B--K38UfxXE2";

    if ((rc = MQTTClient_connect(client, &conn_opts)) != MQTTCLIENT_SUCCESS)
    {
        printf("Failed to connect, return code %d\n", rc);
        exit(EXIT_FAILURE);
    }

    char *Temp;
    char *Humd;
    while(1){
        n = recv(clntSock,buffer,BUFFSIZE,0);
        if ( n<0 )
            error("ERROR reading from socket");
        else if( n>0 ){
            Temp = strtok(buffer, " ");
            Humd = strtok(NULL, " ");
            printf("The Temp and the Humd is: %s %s\n",Temp, Humd);

            //update mysql
            // if (mysql_query(con, "INSERT INTO Writers(Name) VALUES(@buffer)"))
            // {
            //     finish_with_error(con);
            // }

            char buf[1024] = {};
            char query_string[] = {
                "INSERT INTO Writers(Name) VALUES('%s')"
                };

            sprintf(buf, query_string, buffer);
            if (mysql_query(con,buf))
            {
                finish_with_error(con);
            }

            pubmsg.payload = buffer;
            pubmsg.payloadlen = (int)strlen(buffer);
            pubmsg.qos = QOS;
            pubmsg.retained = 0;

            MQTTClient_publishMessage(client, TOPIC, &pubmsg, &token);

            printf("Waiting for up to %d seconds for publication of %s\n"
                    "on topic %s for client with ClientID: %s\n",
                    (int)(TIMEOUT/1000), buffer, TOPIC, CLIENTID);

            rc = MQTTClient_waitForCompletion(client, token, TIMEOUT);
            printf("Message with delivery token %d delivered\n", token);

            //lam gi do
            fflush(stdout);
            bzero(buffer,BUFFSIZE);
        }
        else{
            printf("Client disconnect !\n");
            break;
        }

    }

    close(servSock);

    mysql_close(con);
    exit(0);

    return 0;
}
