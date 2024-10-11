import axiosInstance from "@/commons/libs/axiosInstance";

export const POST_KAKAO_ACCESS_TOKEN_URI = async (code: string) => {
    const response = await axiosInstance.djangoAxiosInst.post(
        "/kakao_oauth/kakao/access-token",
        { code }
    );

    localStorage.setItem("accessToken", response.data.accessToken.access_token);
};

export const POST_KAKAO_USER_INFO = async () => {
    const _accessToken = localStorage.getItem("accessToken");

    const response = await axiosInstance.djangoAxiosInst.post(
        "/kakao_oauth/kakao/user-info",
        { access_token: _accessToken }
    );

    return response.data.user_info;
};

export const POST_EMAIL_DUPLICATION_CHECK = async (email: string) => {
    const response = await axiosInstance.djangoAxiosInst.post(
        "/account/email-duplication-check",
        { email }
    );

    return response.data.isDuplicate;
};
