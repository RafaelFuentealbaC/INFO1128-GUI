var http=require("http");

var manejador=function(solicitud,respuesta){
	console.log("Recibido");
	respuesta.end("Hola que tal");

};

var servidor=http.createServer(manejador);

servidor.listen(8080);