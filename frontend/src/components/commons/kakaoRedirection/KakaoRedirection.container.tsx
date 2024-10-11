import { useEffect } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import KakaoRedirectionPresenter from "./KakaoRedirection.presenter";
import {
    POST_EMAIL_DUPLICATION_CHECK,
    POST_KAKAO_ACCESS_TOKEN_URI,
    POST_KAKAO_USER_INFO,
} from "./KakaoRedirection.queries";

export default function KakaoRedirectionContainer() {
    const router = useRouter();
    const params = useSearchParams();
    const _code = params.get("code");

    useEffect(() => {
        const kakaoRedirectData = async () => {
            if (_code) {
                try {
                    await POST_KAKAO_ACCESS_TOKEN_URI(_code);

                    const _userInfo = await POST_KAKAO_USER_INFO();
                    const email = _userInfo?.kakao_account?.email;

                    const isEmailDuplication =
                        await POST_EMAIL_DUPLICATION_CHECK(email);

                    console.log("123", isEmailDuplication);
                } catch (error) {
                    console.error(
                        "Error ocurred in KakaoRedirectionContainer",
                        error
                    );
                }
            }
        };

        kakaoRedirectData();
    }, [_code]);

    return (
        <>
            <KakaoRedirectionPresenter />
        </>
    );
}
