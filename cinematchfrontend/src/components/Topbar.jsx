import { Menu } from "lucide-react";
import UserAvatar from "./UserAvatar";

const Topbar = ({ title }) => {
    return (
        <div className="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between shadow-sm">
            <div className="flex items-center gap-2">
                <Menu className="w-5 h-5 text-gray-600" />
                <h1 className="text-lg font-semibold text-gray-800">{title}</h1>
            </div>
            <div className="m1-auto">
                <UserAvatar name="Cine Match" />
            </div>
        </div>
    )
};

export default Topbar;
