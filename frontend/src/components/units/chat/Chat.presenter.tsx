import { Toolbar, List, CssBaseline, Divider, IconButton } from "@mui/material";

import * as S from "./Chat.styles";
import MenuIcon from "@mui/icons-material/Menu";
import ChatContainerInput from "./Chat.containerInput";
import ChatPresenterAnimation from "./Chat.presenterAnimation";
import ChatPresenterBacklog from "./Chat.presenterBacklog";
import ChatPresenterError from "./Chat.presenterError";
import { IChatPresenter } from "./Chat.types";

export default function ChatPresenter(props: IChatPresenter) {
    return (
        <>
            <S.ChatWrapper>
                <CssBaseline />
                <props.AppBar open={props._open}>
                    <Toolbar>
                        <S.StyledIconButton
                            open={props._open}
                            color="inherit"
                            aria-label="open drawer"
                            onClick={props.handleDrawerOpen}
                            edge="start"
                        >
                            <MenuIcon />
                        </S.StyledIconButton>
                        <S.LogoTypgraphy noWrap>Si-Follow</S.LogoTypgraphy>
                    </Toolbar>
                </props.AppBar>

                <props.Drawer variant="permanent" open={props._open}>
                    <props.DrawerHeader>
                        <IconButton onClick={props.handleDrawerClose}>
                            {props.theme.direction === "rtl" ? (
                                <S.StyledChevronRightIcon />
                            ) : (
                                <S.StyledChevronLeftIcon />
                            )}
                        </IconButton>
                    </props.DrawerHeader>
                    <Divider />
                    <List>
                        {props._menuItem.map((item, index) => (
                            <S.StyledListItem
                                key={item}
                                disablePadding
                                onClick={() => props.handleClickMenuItem(item)}
                            >
                                <S.StyledListItemButton open={props._open}>
                                    <S.StyledListItemIcon open={props._open}>
                                        {index % props._menuItem.length ===
                                        0 ? (
                                            <S.StyledInputIcon />
                                        ) : index % props._menuItem.length ===
                                          1 ? (
                                            <S.StyledAnimationIcon />
                                        ) : index % props._menuItem.length ===
                                          2 ? (
                                            <S.StyledHistoryIcon />
                                        ) : (
                                            <S.StyledErrorIcon />
                                        )}
                                    </S.StyledListItemIcon>
                                    <S.StyledListItemText
                                        primaryTypographyProps={{
                                            fontSize: "1.6rem",
                                        }}
                                        primary={item}
                                        open={props._open}
                                    />
                                </S.StyledListItemButton>
                            </S.StyledListItem>
                        ))}
                    </List>
                </props.Drawer>

                <S.UserInteractiveBox>
                    <props.DrawerHeader />
                    {props._status === "Input" && (
                        <>
                            <ChatContainerInput />
                        </>
                    )}

                    {props._status === "Animation" && (
                        <>
                            <ChatPresenterAnimation />
                        </>
                    )}

                    {props._status === "Backlog" && (
                        <>
                            <ChatPresenterBacklog />
                        </>
                    )}

                    {props._status === "Error" && (
                        <>
                            <ChatPresenterError />
                        </>
                    )}
                </S.UserInteractiveBox>
            </S.ChatWrapper>
        </>
    );
}
