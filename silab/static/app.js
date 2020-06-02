formularioActivado = new Boolean(false);
solisitudesActivado = new Boolean(false);


function agregar_buscador() {

  // var texto = document.getElementsByTagName("accion");
  // texto[0].innerHTML = "Solisitud de material";

  if (formularioActivado != true) {
    var elemento = document.createElement("input");
    var contenido = document.createTextNode("id");
    elemento.appendChild(contenido);
    elemento.setAttribute("id", "inputId");
    elemento.setAttribute("placeholder", "ID");
    elemento.setAttribute("name", "id_articulo");
    document.getElementById("formulario").appendChild(elemento);

    var elemento = document.createElement("button");
    var contenido = document.createTextNode("Buscar");
    elemento.appendChild(contenido);
    elemento.setAttribute("id", "buttonBuscar");
    elemento.setAttribute("class", "waves-effect waves-light btn white-text");
    document.getElementById("formulario").appendChild(elemento);

    var elemento = document.createElement("button");
    var contenido = document.createTextNode("Otro");
    elemento.appendChild(contenido);
    elemento.setAttribute("id", "buttonOtro");
    elemento.setAttribute("class", "waves-effect waves-light btn white-text");
    document.getElementById("formulario").appendChild(elemento);

    formularioActivado = true;

    var child = document.getElementById("tabla");
    child.parentNode.removeChild(child);




    solisitudesActivado = false;
  }
}



function agregar_solisitudes() {

  // var texto = document.getElementsByTagName("accion");
  // texto[0].innerHTML = "Historial";

  if (solisitudesActivado != true) {
    var elemento = document.createElement("input");
    var contenido = document.createTextNode("Buscar");
    elemento.appendChild(contenido);
    elemento.setAttribute("placeholder", "historial");
    elemento.setAttribute("id", "tabla");
    document.getElementById("solisitudes").appendChild(elemento);

    solisitudesActivado = true;

    var elemento = document.getElementById("inputId");
    elemento.parentNode.removeChild(elemento);
    var elemento = document.getElementById("buttonBuscar");
    elemento.parentNode.removeChild(elemento);
    var elemento = document.getElementById("buttonOtro");
    elemento.parentNode.removeChild(elemento);


    formularioActivado = false;
  }
}
