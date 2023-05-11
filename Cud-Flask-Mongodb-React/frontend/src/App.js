// Importamos react
import React from 'react';

// Importamos algunos modulos de react router dom
import {

  // Importamos browser router y le cambiamos el nombre a Router
  BrowserRouter as Router, 
  
  // Importamos el modulo switch para poder hacer las rutas de la app
  Switch,

  // Importamos el modulo route para poder hacer las rutas de la app
  Route } from 'react-router-dom';
//-------------------------IMPORT COMPONENTS---------------------------//




//-------------------------IMPORT PAGES---------------------------//
function App() {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/"></Route>
        </Switch>
      </div>
    </Router>
  );
}
//-------------------------IMPORT PAGES---------------------------//




//-------------------------EXPORT APP---------------------------//
export default App;
