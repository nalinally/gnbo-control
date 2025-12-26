#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <IcsHardSerialClass.h>

#define EN_PIN 15

const char* ssid = "Shoryu";
const char* password = "ic191209";

const long BAUDRATE = 115200;
const int TIMEOUT = 1000; //通信できてないか確認用にわざと遅めに設定

IcsHardSerialClass krs(&Serial,EN_PIN,BAUDRATE,TIMEOUT);

ESP8266WebServer server(80);

void handleSetPos() {
  if (server.hasArg("id") && server.hasArg("pos")) {
    int id = server.arg("id").toInt();
    float pos = float(server.arg("pos").toInt());
    server.send(200, "text/plain",
        "set id" + String(id) + " servo pos to " + String(pos) + " degree");
    krs.setPos(id, krs.degPos(pos));
  } else {
    server.send(400, "text/plain", "set field [id], [pos]");
  }
}

void handleSetFree() {
  if (server.hasArg("id")) {
    int id = server.arg("id").toInt();
    server.send(200, "text/plain",
        "set id" + String(id) + " servo free");
    krs.setFree(id);
  } else {
    server.send(400, "text/plain", "set field [id]");
  }
}

void handleSetSpd() {
  if (server.hasArg("id") && server.hasArg("spd")) {
    int id = server.arg("id").toInt();
    int spd = server.arg("spd").toInt();
    server.send(200, "text/plain",
        "set id" + String(id) + " servo speed to " + String(spd));
    krs.setSpd(id, spd);
  } else {
    server.send(400, "text/plain", "set field [id], [spd]");
  }
}

void handleSetID() {
  if (server.hasArg("id")) {
    int id = server.arg("id").toInt();
    server.send(200, "text/plain",
        "set id to " + String(id));
    krs.setID(id);
  } else {
    server.send(400, "text/plain", "set field [id]");
  }
}

void handleGetPos() {
  if (server.hasArg("id")) {
    int id = server.arg("id").toInt();
    server.send(200, "text/plain", String(krs.posDeg(krs.getPos(id))));
  } else {
    server.send(400, "text/plain", "set field [id]");
  }
}

void handleGetSpd() {
  if (server.hasArg("id")) {
    int id = server.arg("id").toInt();
    server.send(200, "text/plain", String(krs.getSpd(id)));
  } else {
    server.send(400, "text/plain", "set field [id]");
  }
}

void handleGetID() {
  server.send(200, "text/plain", String(krs.getID()));
}


void setup() {

  // Serial
  Serial.begin(115200);

  // WiFi
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to ");
  Serial.print(ssid);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // server
  server.on("/set_pos", handleSetPos);
  server.on("/set_free", handleSetFree);
  server.on("/set_spd", handleSetSpd);
  server.on("/set_id", handleSetID);
  server.on("/get_pos", handleGetPos);
  server.on("/get_spd", handleGetSpd);
  server.on("/get_id", handleGetID);
  server.begin();

  // LED
  pinMode(LED_BUILTIN, OUTPUT);

  // KRS Servo
  krs.begin(); //サーボモータの通信初期設定

}

void loop() {
  server.handleClient();
}
