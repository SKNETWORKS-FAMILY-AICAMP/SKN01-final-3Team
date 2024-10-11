import { ChangeEvent } from "react";

export interface IChatPresenter {
    theme: any;
    _open: Boolean;
    _status: string;
    _menuItem: Array<string>;
    AppBar: any;
    Drawer: any;
    DrawerHeader: any;
    handleDrawerOpen: () => void;
    handleDrawerClose: () => void;
    handleClickMenuItem: (item: string) => void;
}

export interface IFormInput {
    userToken: string;
    projectName: string;
    config: string;
    requirements: string;
}

export interface IChatPresenterInput {
    _lineHeight: Number;
    _lineCount: Number;
    _containerRef: any;
    register: any;
    handleSubmit: any;
    errors: any;
    onSubmit: (data: IFormInput) => void;
    _isClickSubmit: Boolean;
    _logs: Array<string>;
}
