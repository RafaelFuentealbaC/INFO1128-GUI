var mysql = require('mysql');
 
var client = mysql.createConnection(
    {
      host     : 'localhost',
      user     : 'root',
      password : '',
      database : 'autos',
    }
);
 
client.connect(function(error, results) {
  if(error) {
    console.log('Error de conexion: ' + error.message);
    return;
  }
  console.log('Conectado a MySQL correctamente');
});
 
var io = require('socket.io').listen(15000, { log: false });
 
 
io.sockets.on('connection', function (socket) {
    socket.on('request1', function() {
        client.query("SELECT marca FROM ventas", function(errors, rows) {
            socket.emit('send1', rows[0].type);
        });
    });
});