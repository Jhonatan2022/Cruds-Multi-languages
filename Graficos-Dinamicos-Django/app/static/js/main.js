// Creamos una contante para obtener la opcion del gráfico
const getOptionChart = async () => {
  // Englobamos en un try catch para capturar errores
  try {
    // Creamos una constande y usamos la api nativa de javascript para obtener el json
    const response = await fetch("http://127.0.0.1:8000/barchart/");

    // Creamos una constante para obtener el json
    return await response.json();

    // Usamos catch para capturar errores
  } catch (error) {
    // Mostramos el error en consola
    alert(error);
  }
};

// Creamos una constante asincrona para obtener el id del gráfico
const initChar = async () => {
  // Obtenemos el id del gráfico
  // Init es para inicializar el gráfico en el html
  // Echarts es un elemento global que se crea automaticamente cuando se importa la libreria
  const idChart = echarts.init(document.getElementById("chart"));

  // Creamos una constante para obtener la opcion del gráfico
  idChart.setOption(await getOptionChart());

  // Usamos rezise para que el gráfico se adapte al tamaño de la pantalla
  idChart.resize();
};

// Creamos un evento de escucha para cuando se cargue el documento
window.addEventListener("load", async () => {
  // Cargamos el gráfico
  await initChar();
});
