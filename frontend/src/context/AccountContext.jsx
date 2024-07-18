import { createContext } from "react";
const AccountContext = createContext({access_token: localStorage.getItem('access_token')});

export default AccountContext;