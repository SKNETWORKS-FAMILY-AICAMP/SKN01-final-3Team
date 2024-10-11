import React, { useEffect, useState } from "react";
import HomePresenter from "./Home.presenter";

export default function HomeContainer() {
    const [_pressedKey, setPressedKey] = useState<string | null>(null);

    useEffect(() => {
        const onKeyDown = (event: KeyboardEvent) => {
            const keyMap: { [key: string]: string } = {
                "1": "keyboard1",
                "2": "keyboard2",
                "3": "keyboard3",
                "4": "keyboard4",
                "5": "keyboard5",
                "6": "keyboard6",
                "7": "keyboard7",
                "8": "keyboard8",
                "9": "keyboard9",
                "0": "keyboard0",
                q: "keyboardQ",
                w: "keyboardW",
                e: "keyboardE",
                r: "keyboardR",
                t: "keyboardT",
                y: "keyboardY",
                u: "keyboardU",
                i: "keyboardI",
                o: "keyboardO",
                p: "keyboardP",
                a: "keyboardA",
                s: "keyboardS",
                d: "keyboardD",
                f: "keyboardF",
                g: "keyboardG",
                h: "keyboardH",
                j: "keyboardJ",
                k: "keyboardK",
                l: "keyboardL",
                z: "keyboardZ",
                x: "keyboardX",
                c: "keyboardC",
                v: "keyboardV",
                b: "keyboardB",
                n: "keyboardN",
                m: "keyboardM",
                ㅂ: "keyboardQ",
                ㅈ: "keyboardW",
                ㄷ: "keyboardE",
                ㄱ: "keyboardR",
                ㅅ: "keyboardT",
                ㅛ: "keyboardY",
                ㅕ: "keyboardU",
                ㅑ: "keyboardI",
                ㅐ: "keyboardO",
                ㅔ: "keyboardP",
                ㅁ: "keyboardA",
                ㄴ: "keyboardS",
                ㅇ: "keyboardD",
                ㄹ: "keyboardF",
                ㅎ: "keyboardG",
                ㅗ: "keyboardH",
                ㅓ: "keyboardJ",
                ㅏ: "keyboardK",
                ㅣ: "keyboardL",
                ㅋ: "keyboardZ",
                ㅌ: "keyboardX",
                ㅊ: "keyboardC",
                ㅍ: "keyboardV",
                ㅠ: "keyboardB",
                ㅜ: "keyboardN",
                ㅡ: "keyboardM",
            };

            const mappedKey = keyMap[event.key.toLowerCase()];

            if (mappedKey) {
                setPressedKey(mappedKey);
            }
        };

        const onKeyUp = () => {
            setPressedKey(null);
        };

        window.addEventListener("keydown", onKeyDown);
        window.addEventListener("keyup", onKeyUp);

        return () => {
            window.removeEventListener("keydown", onKeyDown);
            window.removeEventListener("keyup", onKeyUp);
        };
    }, [_pressedKey]);

    return (
        <>
            <HomePresenter _pressedKey={_pressedKey} />
        </>
    );
}
