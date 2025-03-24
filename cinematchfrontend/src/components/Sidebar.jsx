const Sidebar = () => {
    return (
        <div className="w-64 h-screen bg-gray-800 text-white p-4">
            <h2 className="text-2x1 font-bold mb-6">Cinematch</h2>
            <nav className="flex flex-col gap-4">
                <a href="#" className="hover:bg-gray-700 p-2 rounded">Dashboard</a>
                <a href="#" className="hover:bg-gray-700 p-2 rounded">Configurações</a>
                <a href="#" className="hover:bg-gray-700 p-2 rounded">Perfil</a>
                <a href="#" className="hover:bg-gray-700 p-2 rounded">Logout</a>
            </nav>
        </div>
    )
}

export default Sidebar;