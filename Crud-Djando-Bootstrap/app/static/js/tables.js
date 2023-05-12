//------------------------------------REQUEST API------------------------------------
// Creamos una variable para saber si esta iniciada la tabla
let dataTable;

// Creamos un variable para saver si esta inicializada la tabla y dejamos predeterminado false
let dataTableIsInitialized = false;

// Creamos una constante para las opciones de la tabla
const options = {

    // Obtenemos las columnas y les asignamos una clase a todas
    columnDefs: [

        // Usamos targets para indicar a que columnas le vamos a asignar una clase
        { classNmane: "bg-secondary", targets: [0, 1, 2, 3, 4, 5, 6]},

        // Orderable sirve para indicar si la columna es ordenable o no
        { orderable: false, targets: [5, 6]},

        // Searchable sirve para indicar si la columna es buscable o no
        { searchable: false, targets: [0, 5, 6]}
    ],
    // Indicamos cuantas filas queremos que se muestren por pagina
    pageLength: 4,

    // Indicamos que queremos que se muestre en la tabla
    detroy: true,
};

// Creamos una constante asncrona para saber si esta inicializada la tabla
const initDataTable = async () => {

    // Si la tabla esta inicializada (True) 
    if (dataTableIsInitialized){

        // Destruimos la tabla
        // Destroy sirve para destruir la tabla y volver a crearla
        dataTable.destroy();
    } 

    // Llamamos la funcion ListProgramers cuando se cargue la pagina
    await listProgramers();

    // Usamos jQuery para seleccionar la tabla y le pasamos el id de la tabla
    // Usamos DataTable para inicializar la tabla y le pasamos un objeto con las opciones
    dataTable = $('#datatable-programers').DataTable(options);

    // Cambiamos el valor de la variable a true
    dataTableIsInitialized = true;
};


// Creamos una constante asincrona con funcion flecha
const listProgramers = async () => {

    // Englobamos el codigo en un try catch para capturar los errores
    try {

        // Creamos una constante que recibe la respuesta de la API
        // Usamos await para esperar la respuesta de la API
        // Usamos fetch para hacer la peticion a la API y le pasamos la url de la API
        const response = await fetch('http://127.0.0.1:8000/app/list_programers/');

        // Creamos una constante que recibe los datos de la API y los convertimos a JSON
        // Usamos await para esperar la respuesta de la API
        // Usamos json para convertir los datos a JSON
        const data = await response.json();

        // Declaramos una variable que recibe el elemento del DOM donde vamos a mostrar los datos
        let content = ``;

        // Convertimos data en un array y usamos forEach para recorrerlo y mostrarlo en el DOM
        data.programers.forEach((programer, index) => {

            // Usamos += para agregar los datos al elemento del DOM
            // Indicamos index +1 para que el id no comience en 0
            content += `
                <tr>
                    <td class="text-center">${index + 1}</td>
                    <td class="text-center">${programer.name}</td>
                    <td class="text-center">${programer.country}</td>
                    <td class="text-center">${programer.birthday}</td>
                    <td class="text-center">${programer.score}</td>
                    <td class="text-center">${programer.score > 6 
                        ? "<i class='fa-solid fa-file-shield text-success'></i>" 
                        : "<i class='fa-solid fa-box-archive text-danger'></i>"} </td>
                    <td class="text-center">
                        <button class="btn btn-sm btn-primary"><i class="fas fa-edit text-light"></i></button>
                        <button class="btn btn-sm btn-danger"><i class="fas fa-trash"></i></button>
                    </td>
                </tr>
                `;
        });

        // Usamos innerHTML para mostrar los datos en el DOM y le pasamos la variable content
        tableBody_programers.innerHTML = content;


    // Usamos catch para capturar los errores y le pasamos el error
    }catch (error) {

        // Usamos console.log para mostrar el error en la consola
        alert(error);
        }
};


// Creamos un evento de escucha asincrono con funcion flecha
// AddEventListener es un metodo que nos permite agregar un evento de escucha a un elemento del DOM
window.addEventListener("load", async () => {

    // Llamamos la funcion initDataTable cuando se cargue la pagina
    await initDataTable();

});
//------------------------------------REQUEST API------------------------------------