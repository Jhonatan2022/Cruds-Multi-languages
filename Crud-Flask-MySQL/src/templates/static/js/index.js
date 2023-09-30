// Usaremos el componente ThemeProvider de styled-components para poder cambiar el tema de nuestra aplicación
// creamos una constante con funcion flecha que recibe un objeto con un children y un tema
const themaC = () => {
  // Seleccionamos el body y le agregamos el tema que recibimos por props
  // Usamos setAttribute para agregar un atributo al body y le pasamos el nombre del atributo y el valor
  // Usamos querySelector para seleccionar el body
  document.querySelector("body").setAttribute("data-bs-theme", "light");

  // Seleccionamos el boton y su id para cambiar también el icono
  // Usamos querySelector para seleccionar el boton
  // Usamos setAttribute para agregar un atributo al boton y le pasamos el nombre del atributo y el valor
  document.querySelector("#modo").setAttribute("class", "fas fa-moon");
};

const themaO = () => {
  // Seleccionamos el body y le agregamos el tema que recibimos por props
  // Usamos setAttribute para agregar un atributo al body y le pasamos el nombre del atributo y el valor
  // Usamos querySelector para seleccionar el body
  document.querySelector("body").setAttribute("data-bs-theme", "dark");

  // Seleccionamos el boton y su id para cambiar también el icono
  // Usamos querySelector para seleccionar el boton
  // Usamos setAttribute para agregar un atributo al boton y le pasamos el nombre del atributo y el valor
  document.querySelector("#modo").setAttribute("class", "fas fa-sun");
};

// Creamos una constante con funcion flecha que recibe el tema actual y pueda alternar entre los temas
const alternarTema = () => {
  // Usamos querySelector para seleccionar el body y le pasamos el tema actual
  // Usamos getAttribute para obtener el valor del atributo que le pasamos
  document.querySelector("body").getAttribute("data-bs-theme") === "dark"
    ? themaC()
    : themaO();
};
