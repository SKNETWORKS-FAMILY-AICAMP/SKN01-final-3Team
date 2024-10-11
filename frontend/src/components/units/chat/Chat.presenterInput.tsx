import { RadioGroup } from "@mui/material";
import * as S from "./Chat.styles";
import { IChatPresenterInput } from "./Chat.types";

export default function ChatPresenterInput(props: IChatPresenterInput) {
    return (
        <S.ChatPresenterInputBox>
            <S.FileBox>
                <S.FileNameBox>
                    Input.html
                    <S.StyledCloseIcon />
                </S.FileNameBox>
                <S.FileNameBox2>Input.js</S.FileNameBox2>
                <S.FileNameBox2>Input.css</S.FileNameBox2>
            </S.FileBox>

            <S.UserInputBox>
                <S.LineNumberBox ref={props._containerRef}>
                    {Array.from(
                        { length: Number(props._lineCount) },
                        (_, index) => (
                            <span
                                key={index}
                                style={{
                                    display: "block",
                                    height: `${props._lineHeight}px`,
                                }}
                            >
                                {index + 1}
                            </span>
                        )
                    )}
                </S.LineNumberBox>

                <S.StyledForm
                    onSubmit={props.handleSubmit((data: any) => {
                        props.onSubmit(data);
                    })}
                >
                    <S.UserInput>
                        <S.InputBox>
                            <S.StyledTypography>
                                유저 토큰 값
                            </S.StyledTypography>
                            <S.StyledTextField
                                {...props.register("userToken")}
                                value="UserToken123456"
                                disabled
                            />
                        </S.InputBox>

                        <S.InputBox>
                            <S.StyledTypography>
                                프로젝트 이름
                            </S.StyledTypography>
                            <S.StyledTextField
                                {...props.register("projectName", {
                                    required: "프로젝트 이름을 입력해주세요 !",
                                })}
                                placeholder="프로젝트 이름을 입력해주세요 !"
                            />
                            {props.errors.projectName && (
                                <S.InputError>
                                    {props.errors.projectName.message}
                                </S.InputError>
                            )}
                        </S.InputBox>

                        <S.StyledFormControl>
                            <S.StyledFormLabel>Config 설정</S.StyledFormLabel>
                            <RadioGroup row defaultValue="default1">
                                <S.StyledFormControlLabel
                                    value="default1"
                                    control={<S.StyledRadio />}
                                    label="default1"
                                    {...props.register("config")}
                                />
                                <S.StyledFormControlLabel
                                    value="default2"
                                    control={<S.StyledRadio />}
                                    label="default2"
                                    {...props.register("config")}
                                />
                            </RadioGroup>
                        </S.StyledFormControl>

                        <S.InputBox>
                            <S.StyledTypography>요구사항</S.StyledTypography>
                            <S.StyledTextField
                                {...props.register("requirements", {
                                    required: "요구사항을 입력해주세요 !",
                                })}
                                multiline
                                minRows={4}
                                maxRows={4}
                            />
                            {props.errors.requirements && (
                                <S.InputError>
                                    {props.errors.requirements.message}
                                </S.InputError>
                            )}
                        </S.InputBox>
                    </S.UserInput>
                    <S.SubmitButtonBox>
                        <S.SubmitButton variant="contained" type="submit">
                            보내기
                        </S.SubmitButton>
                    </S.SubmitButtonBox>
                </S.StyledForm>
            </S.UserInputBox>

            <S.TerminalBox>
                {!props._isClickSubmit &&
                    props._logs.map((log, index) => (
                        <div key={index}>{log}</div>
                    ))}
                {props._isClickSubmit && <div>〉〉〉 Compiling...</div>}
            </S.TerminalBox>
        </S.ChatPresenterInputBox>
    );
}
