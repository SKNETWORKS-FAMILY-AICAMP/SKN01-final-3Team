import styled from "@emotion/styled";

// HomePresenter
export const HomeWrapper = styled.div`
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    background-color: #202020;
`;

export const HomePresenterHeroWrapper = styled.div`
    width: 33.4rem;
    height: 21.6rem;
    overflow-y: hidden;
`;

// HomePresenterHero
export const HeroWrapper = styled.div`
    width: 100%;
    height: 100%;
`;

export const LoginText = styled.div`
    width: 100%;
    display: flex;
    justify-content: center;
    padding-top: 2rem;
`;

export const HeroVideo = styled.video`
    width: 100%;
    height: 100%;
    object-fit: cover;
`;

export const HeroButton = styled.button`
    position: absolute;
    margin-bottom: 0.5rem;
    left: 50%;
    bottom: 0;
    transform: translateX(-50%);
`;
