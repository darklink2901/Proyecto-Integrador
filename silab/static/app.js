// formularioActivado = new Boolean(false);
// solisitudesActivado = new Boolean(false);
//
//
// function agregar_buscador() {
//   // var texto = document.getElementsByTagName("accion");
//   // texto[0].innerHTML = "Solisitud de material";
//
//   if (formularioActivado != true) {
//
//     var elemento = document.createElement("input");
//     var contenido = document.createTextNode("id");
//     elemento.appendChild(contenido);
//     elemento.setAttribute("id", "inputId");
//     elemento.setAttribute("placeholder", "ID");
//     elemento.setAttribute("name", "id_articulo");
//     document.getElementById("formulario").appendChild(elemento);
//
//     var elemento = document.createElement("button");
//     var contenido = document.createTextNode("Buscar");
//     elemento.appendChild(contenido);
//     elemento.setAttribute("id", "buttonBuscar");
//     elemento.setAttribute("class", "waves-effect waves-light btn white-text");
//     document.getElementById("formulario").appendChild(elemento);
//
//
//     var elemento = document.createElement("button");
//     var contenido = document.createTextNode("Otro");
//     elemento.appendChild(contenido);
//     elemento.setAttribute("id", "buttonOtro");
//     elemento.setAttribute("onclick", "agregar_otro();");
//     elemento.setAttribute("class", "waves-effect waves-light btn white-text");
//     document.getElementById("otro-material").appendChild(elemento);
//
//
//
//     formularioActivado = true;
//
//     var child = document.getElementById("tabla");
//     child.parentNode.removeChild(child);
//
//
//
//
//     solisitudesActivado = false;
//   }
// }
//
//
//
// function agregar_solisitudes() {
//
//   // var texto = document.getElementsByTagName("accion");
//   // texto[0].innerHTML = "Historial";
//
//   if (solisitudesActivado != true) {
//     var elemento = document.createElement("input");
//     var contenido = document.createTextNode("Buscar");
//     elemento.appendChild(contenido);
//     elemento.setAttribute("placeholder", "historial");
//     elemento.setAttribute("id", "tabla");
//     document.getElementById("solisitudes").appendChild(elemento);
//
//     solisitudesActivado = true;
//
//     var elemento = document.getElementById("inputId");
//     elemento.parentNode.removeChild(elemento);
//     var elemento = document.getElementById("buttonBuscar");
//     elemento.parentNode.removeChild(elemento);
//     var elemento = document.getElementById("buttonOtro");
//     elemento.parentNode.removeChild(elemento);
//
//
//     formularioActivado = false;
//   }
// }
//
// function agregar_otro(){
//   var elemento = document.getElementById("inputId");
//   elemento.parentNode.removeChild(elemento);
//   var elemento = document.getElementById("buttonBuscar");
//   elemento.parentNode.removeChild(elemento);
//   var elemento = document.getElementById("buttonOtro");
//   elemento.parentNode.removeChild(elemento);
//
//   formularioActivado = false;
//
//   var elemento = document.createElement("label");
//   var contenido = document.createTextNode("Nombre");
//   elemento.appendChild(contenido);
//   document.getElementById("solisitudes").appendChild(elemento);
//
//   var elemento = document.createElement("input");
//   var contenido = document.createTextNode("Buscar");
//   elemento.appendChild(contenido);
//   elemento.setAttribute("placeholder", "Articulo");
//   document.getElementById("solisitudes").appendChild(elemento);
//
//   // -----------------------------------------------------------
//
//   var elemento = document.createElement("label");
//   var contenido = document.createTextNode("Cantidad");
//   elemento.appendChild(contenido);
//   document.getElementById("solisitudes").appendChild(elemento);
//
//   var elemento = document.createElement("input");
//   var contenido = document.createTextNode("Buscar");
//   elemento.appendChild(contenido);
//   elemento.setAttribute("placeholder", "Cantidad");
//   document.getElementById("solisitudes").appendChild(elemento);
//
//   // ------------------------------------------------------------
//
//   var elemento = document.createElement("label");
//   var contenido = document.createTextNode("Precio");
//   elemento.appendChild(contenido);
//   document.getElementById("solisitudes").appendChild(elemento);
//
//   var elemento = document.createElement("input");
//   var contenido = document.createTextNode("Buscar");
//   elemento.appendChild(contenido);
//   elemento.setAttribute("placeholder", "Precio");
//   document.getElementById("solisitudes").appendChild(elemento);
// }



function solisitar() {
    var div_entregas = document.getElementById("entregas");


    var div_prestamos = document.getElementById("prestamos");
    if (div_prestamos.style.display === "none") {

        div_prestamos.style.display = "block";
        div_entregas.style.display = "none";

    } else {
        div_prestamos.style.display = "none";
    }
}


function entregar() {
  var div_prestamos = document.getElementById("prestamos");

  var div_entregas = document.getElementById("entregas");
  if (div_entregas.style.display === "none") {

      div_entregas.style.display = "block";
      div_prestamos.style.display = "none";
  } else {
      div_entregas.style.display = "none";
  }

}
