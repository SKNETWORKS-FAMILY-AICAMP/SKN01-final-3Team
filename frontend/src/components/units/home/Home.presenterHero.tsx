import * as S from "./Home.styles";
import { IHomePresenterHero } from "./Home.types";

export default function HomePresenterHero(props: IHomePresenterHero) {
    return (
        <>
            <S.HeroWrapper>
                {props._isClickedLogin ? (
                    <>
                        <S.LoginText>로그인</S.LoginText>
                        {props.IconBox}
                    </>
                ) : (
                    <>
                        <S.HeroVideo
                            src="/videos/space.mp4"
                            autoPlay
                            muted
                            loop
                        />
                        <S.HeroButton onClick={props.onChangeIsClickedLogin}>
                            시작하기
                        </S.HeroButton>
                    </>
                )}
            </S.HeroWrapper>
        </>
    );
}
