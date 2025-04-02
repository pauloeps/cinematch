import Sidebar from './components/Sidebar';
import Reviews from './pages/Reviews';
import Settings from './pages/Settings';
import Topbar from './components/Topbar';
import Dashboard from './pages/Dashboard';
import { Routes, Route, useLocation } from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';

function LayoutWithSidebar() {
  const location = useLocation();

  const getPageTitle = (pathname) => {
    switch (pathname) {
      case "/":
        return "Dashboard";
      case "/reviews":
        return "Reviews";
      case "/settings":
        return "Configurações";
      default:
        return "Cinematch";
    }
  }
  
  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex flex-col flex-1 overflow-hidden">
        <Topbar title={getPageTitle(location.pathname)}/>
        <div className="flex-1 overflow-y-auto p-4 bg-gray-100">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/reviews" element={<Reviews />} />
            <Route path="/settings" element={<Settings />} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <LayoutWithSidebar />
    </Router>
  )
}

export default App
