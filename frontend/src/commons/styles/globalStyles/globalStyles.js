// 전역 스타일 설정하는 곳
import { css } from "@emotion/react";

// 반응형 설정 때 주로 사용하는 사이즈 설정법에는 em, rem, vw, % 등이 있지만,
// rem을 사용할 때 아래와 같이 font-size: 62.5%로 설정하고, 이는 10px에 해당됨
// 따라서 아래와 같이 설정해놓으면, 1rem = 10px, 10rem = 100px이 됨.
// font-size: 100%로 설정하게되면 1rem = 16px이 됨.
// 이렇게만 한다고 반응형 설정하는게 아님.
// 잘 모르겟으면 영훈한테 찾아오셈.
export const globalStyles = css`
    html,
    body,
    main,
    #root {
        width: 100%;
        height: 100%;
        margin: 0;
        padding: 0;
        font-size: 62.5%;
    }

    #__next {
        width: 100%;
        height: 100%;
    }
`;
