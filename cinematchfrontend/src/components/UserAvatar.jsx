import { useState, useRef, useEffect } from "react";

const UserAvatar = ({ name }) => {
    const [open, setOpen] = useState(false);
    const avatarRef = useRef();

    const initials = name
        .split(" ")
        .map((n) => n[0])
        .join("")
        .toUpperCase();

    useEffect(() => {
        const handleClickOutside = (event) => {
            if (avatarRef.current && !avatarRef.current.contains(event.target)) {
                setOpen(false);
            }
        };

        document.addEventListener("mousedown", handleClickOutside);
        return () => document.removeEventListener("mousedown", handleClickOutside);
    }, [])

    return (
        <div className="relative" ref={avatarRef}>
            <div
                onClick={() => setOpen(!open)}
                className="w-10 h-10 rounded-full bg-gray-300 text-white flex items-center justify-center font-semibold cursor-pointer"
            >
                {initials}
            </div>

            {open && (
                <div className="absolute right-0 mt-2 w-50 bg-white border border-gray-200 rounded-md shadow-lg z-50">
                    <ul className="py-2 text-sm text-gray-700">
                        <li className="px-4 py-2 hover:bg-gray-100 cursor-pointer">Perfil</li>
                        <li className="px-4 py-2 hover:bg-gray-100 text-red-600 hover:bg-red-50 hover:text-red-700 cursor-pointer">Logout</li>
                    </ul>
                </div>
            )}
        </div>
    );
};

export default UserAvatar;