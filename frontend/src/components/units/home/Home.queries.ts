import axiosInstance from "@/commons/libs/axiosInstance";

export const GET_KAKAO_OAUTH_URI = async () => {
    return await axiosInstance.djangoAxiosInst
        .get("/kakao_oauth/kakao")
        .then((res) => {
            window.location.href = res.data.url;
        });
};
