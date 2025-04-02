import { Link, useLocation } from "react-router-dom";
import { LayoutDashboard, Settings, ClipboardList } from "lucide-react";

const Sidebar = () => {
    const location = useLocation();
    const menuItems = [
        { name: "Dashboard", to: "/", icon: <LayoutDashboard className="w-5 h-5" />},
        { name: "Reviews", to: "/reviews", icon: <ClipboardList className="w-5 h-5" />},
        { name: "Configurações", to: "/settings", icon: <Settings className="w-5 h-5" /> },
    ]

    return (
        <div className="w-64 h-full bg-gray-50 border-r border-gray-200 p-6 text-gray-600">
            <h2 className="text-2x1 text-lg font-bold mb-10">Cinematch</h2>
            <nav className="flex flex-col gap-3">
                {menuItems.map(({ name, to, icon }) => (
                    <Link
                        key={name}
                        to={to}
                        className={`flex itemx-center gap-3 px-4 py2 rounded hover:bg-gray-200
                        ${
                            location.pathname === to ? "bg-gray-200 font-semibold" : ""
                        }`}
                    >
                        {icon}
                        {name}
                    </Link>
                ))}
            </nav>
        </div>
    )
}

export default Sidebar;