import React, { Suspense } from 'react';
import { Route, Routes, Navigate } from 'react-router-dom';
import { ApiProvider } from './context/ProjectContext';
import PrivateRoute from './components/Commons/privateRoute';
const MainLayout = React.lazy(() => import('./layout/mainLayout'));
const Landing = React.lazy(() => import('./views/Landing/landing'));
const Contacto = React.lazy(() => import('./views/Landing/contacto'));
const Login = React.lazy(() => import('./views/Users/login/login'));
const BancoProyectos = React.lazy(() => import('./views/Projects/bancodeproyectos/bancodeproyectos'));
const BancoIdeas = React.lazy(() => import('./views/Projects/proyectosinnovadores/proyectosInnovadores'));
const Documentacion = React.lazy(() => import('./views/Projects/documentacion/documentacion'));
const Proyecto = React.lazy(() => import('./views/Projects/proyecto/proyecto'));
const ErrorLayout = React.lazy(() => import('./layout/errorLayout'));
const Error404 = React.lazy(() => import('./views/Error/error404'));
const Error500 = React.lazy(() => import('./views/Error/error500'));
const Error503 = React.lazy(() => import('./views/Error/error503'));

function App()
{
  return (
    <ApiProvider>
        <Suspense fallback={<div>Loading...</div>}>
            <Routes>
              <Route path="/" element={<MainLayout />}>
                <Route index element={<Landing />} />
                <Route path="bancodeproyectos" element={<BancoProyectos />} />
                <Route path="bancodeideas" element={<BancoIdeas/>}/>
                <Route path="documentacion" element={<Documentacion />}/>
                <Route path="project/:slug" element={<Proyecto />} />
                <Route path="contacto" element={<Contacto />} />
                <Route path="login" element={<Login />} />
                <Route path="*" element={<Navigate to="/error/error404" />} />
              </Route>
              <Route path="error" element={<ErrorLayout />}>
                <Route path="error404" element={<Error404 />} />
                <Route path="error500" element={<Error500 />} />
                <Route path="error503" element={<Error503 />} />
              </Route>
            </Routes>
        </Suspense>
    </ApiProvider>
  );
}

export default App;