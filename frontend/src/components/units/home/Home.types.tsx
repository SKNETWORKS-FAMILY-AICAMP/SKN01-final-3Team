import { MouseEvent, ReactNode } from "react";

export interface IHomePresenter {
    _pressedKey: string | null;
}

export interface IHomeContainerModel {
    _pressedKey: string | null;
}

export interface IHomePresenterModel {
    _pressedKey: string | null;
    _group: any;
    nodes: any;
    materials: any;
    _keyboardKeys: Array<string>;
    _pressedColor: any;
    _isClickedLogin: Boolean;
    onChangeIsClickedLogin: () => void;
}

export interface IHomeContainerHero {
    _isClickedLogin: Boolean;
    onChangeIsClickedLogin: () => void;
}

export interface IHomePresenterHero {
    _isClickedLogin: Boolean;
    onChangeIsClickedLogin: () => void;
    IconBox: ReactNode;
}
