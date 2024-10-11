import styled from "@emotion/styled";
import {
    Box,
    Button,
    FormControl,
    FormControlLabel,
    FormLabel,
    IconButton,
    ListItem,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Radio,
    TextField,
    Typography,
} from "@mui/material";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";
import InputIcon from "@mui/icons-material/Input";
import AnimationIcon from "@mui/icons-material/Animation";
import HistoryIcon from "@mui/icons-material/History";
import ErrorIcon from "@mui/icons-material/Error";
import CloseIcon from "@mui/icons-material/Close";

// Chat.presenter.tsx
export const ChatWrapper = styled(Box)`
    display: flex;
`;

export const StyledIconButton = styled(IconButton)<{ open: Boolean }>`
    margin-right: 4rem;
    ${(props) => props.open && `display: none;`}
`;

export const LogoTypgraphy = styled(Typography)`
    font-size: 2.4rem;
`;

export const StyledChevronRightIcon = styled(ChevronRightIcon)`
    color: #676e95;
`;

export const StyledChevronLeftIcon = styled(ChevronLeftIcon)`
    font-size: 2.4rem;
    color: #676e95;
`;

export const StyledListItemButton = styled(ListItemButton)<{ open: Boolean }>`
    min-height: 4.8rem;
    padding-left: 2rem;
    padding-right: 2rem;
    ${(props) =>
        props.open ? `justify-content: initial` : `justify-content: center`}
`;

export const StyledListItem = styled(ListItem)`
    dispaly: block;
`;

export const StyledListItemIcon = styled(ListItemIcon)<{ open: Boolean }>`
    min-width: 0;
    display: flex;
    justify-content: center;
    ${(props) => (props.open ? `margin-right: 2.4rem` : `margin-right: auto`)}
`;

export const StyledInputIcon = styled(InputIcon)`
    font-size: 2.4rem;
    color: #676e95;
`;

export const StyledAnimationIcon = styled(AnimationIcon)`
    font-size: 2.4rem;
    color: #676e95;
`;

export const StyledHistoryIcon = styled(HistoryIcon)`
    font-size: 2.4rem;
    color: #676e95;
`;

export const StyledErrorIcon = styled(ErrorIcon)`
    font-size: 2.4rem;
    color: #676e95;
`;

export const StyledListItemText = styled(ListItemText)<{ open: Boolean }>`
    ${(props) => (props.open ? `opacity: 1` : `opacity: 0`)};
    font-weight: bold;
    color: #676e95;
    font-size: 2.4rem;
`;

export const UserInteractiveBox = styled(Box)`
    height: 100vh;
    flex-grow: 1;
    background-color: #292d3e;
`;

// Chat.presenterInput.tsx
export const ChatPresenterInputBox = styled(Box)`
    display: flex;
    flex-direction: column;
`;

export const FileBox = styled(Box)`
    height: 4rem;
    display: flex;
`;

export const FileNameBox = styled(Box)`
    width: fit-content;
    height: 3rem;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    border-bottom: 1px solid #eeffff;
    font-size: 1.6rem;
    color: #eeffff;
`;

export const FileNameBox2 = styled(Box)`
    width: fit-content;
    height: 3rem;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    font-size: 1.6rem;
    color: #717cb470;
`;

export const StyledCloseIcon = styled(CloseIcon)`
    margin-left: 1.2rem;
`;

export const UserInputBox = styled(Box)`
    height: calc(100vh - 25.4rem);
    max-height: calc(100vh - 25.4rem);
    overflow: auto;

    display: flex;
`;

export const LineNumberBox = styled(Box)`
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    position: relative;
    padding-left: 1rem;
    padding-right: 2rem;
    overflow: hidden;
    font-size: 1.6rem;
    color: #414863;
`;

export const StyledForm = styled.form`
    width: 100%;
`;

export const UserInput = styled(Box)`
    display: flex;
    width: 100%;
    flex-direction: column;
    padding-top: 1rem;
    padding-right: 2rem;
`;

export const InputBox = styled(Box)`
    display: flex;
    flex-direction: column;
    margin-bottom: 2rem;
`;

export const StyledTypography = styled(Typography)`
    font-size: 1.8rem;
    color: #89ddff;
    margin-bottom: 0.5rem;
`;

export const StyledTextField = styled(TextField)`
    & .MuiOutlinedInput-root {
        color: #eeffff;

        & fieldset {
            border-color: #82aaff;
        }

        &:hover fieldset {
            border-color: #ffcb6b;
        }

        &.Mui-focused fieldset {
            border-color: #c3e88d;
        }

        &.Mui-disabled fieldset {
            border-color: #82aaff;
        }
    }

    & .MuiOutlinedInput-input.Mui-disabled {
        color: #676e95 !important;
        -webkit-text-fill-color: #676e95 !important;
    }

    & .MuiOutlinedInput-input {
        font-size: 1.6rem;
    }

    & .MuiOutlinedInput-input::placeholder {
        font-size: 1.6rem;
        color: #ffcb6b;
    }
`;

export const InputError = styled(Box)`
    font-size: 1.6rem;
    color: #ff5370;
`;

export const SubmitButtonBox = styled(Box)`
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 5rem;
`;

export const SubmitButton = styled(Button)`
    width: 30%;
    height: 4rem;
    display: flex;
    justify-content: center;
    font-size: 1.8rem;
    font-weight: bold;
    background-color: #ffcb6b;
    transition: background-color 0.3s ease;

    &:hover {
        background-color: #c3e88d;
    }

    &:active {
        background-color: #f78c6c;
    }
`;

export const StyledFormControl = styled(FormControl)`
    margin-bottom: 2rem;
`;

export const StyledFormLabel = styled(FormLabel)`
    font-size: 1.6rem;
    color: #89ddff;

    &.Mui-focused {
        color: #89ddff; // 여기서 원하는 색상으로 수정 가능
    }
`;

export const StyledFormControlLabel = styled(FormControlLabel)`
    & .MuiFormControlLabel-label {
        font-size: 1.6rem;
        color: #eeffff;
    }
`;

export const StyledRadio = styled(Radio)`
    & .MuiSvgIcon-root {
        color: #ffcb6b;
        font-size: 2.4rem;
    }

    &.Mui-checked .MuiSvgIcon-root {
        color: #c3e88d;
    }
`;

export const TerminalBox = styled(Box)`
    width: 100%;
    max-width: 100%;
    height: 15rem;
    max-height: 15rem;
    padding: 1rem;
    overflow: auto;
    font-size: 1.6rem;
    color: #eeffff;
    background-color: #444267;
`;
