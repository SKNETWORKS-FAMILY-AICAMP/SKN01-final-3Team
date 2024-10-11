import type { AppProps } from "next/app";
import { Global } from "@emotion/react";
import { globalStyles } from "@/commons/styles/globalStyles/globalStyles";

function App({ Component, pageProps }: AppProps) {
    return (
        <>
            <Global styles={globalStyles} />
            <Component {...pageProps} />
        </>
    );
}

export default App;
