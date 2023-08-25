import { create } from "zustand";
import { persist } from "zustand/middleware";

type State = {
  access: string;
  refresh: string;
  isAuth: boolean;
};

type Actions = {
  setToken: (access: string, refresh: string) => void;
  logout: () => void;
};

//create defino el almacenamiento con el estado inicial y las acciones asociadas.
export const useAuthStore = create(
  //Config del almacen
  persist<State & Actions>(
    //Estado inicial
    (set) => ({
      access: "",
      refresh: "",
      isAuth: false,
      // Acción para establecer los tokens y la autenticación
      setToken: (access: string, refresh: string) =>
        set(() => ({
          access,
          refresh,
          isAuth: !!access && !!refresh,
        })),
      // Acción para establecer los tokens y la autenticación
      logout: () =>
        set(() => ({
          access: "",
          refresh: "",
          isAuth: false,
        })),
    }),
    {
      name: "auth", //Nombre para la persistencia
    }
  )
);
