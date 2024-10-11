import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import ChatPresenterInput from "./Chat.presenterInput";

export default function ChatContainerInput() {
    const _lineHeight = 20;
    const _containerRef = useRef(null);
    const [_lineCount, setLineCount] = useState(0);
    const [_isClickSubmit, setIsClickSubmit] = useState(false);
    const [_logs, setLogs] = useState<string[]>([]);

    const {
        register,
        handleSubmit,
        formState: { errors },
        reset,
        watch,
        setValue,
    } = useForm({
        defaultValues: {
            userToken: "UserToken123456",
            projectName: "",
            config: "default1",
            requirements: "",
        },
    });

    const projectName = watch("projectName");
    const config = watch("config");
    const requirements = watch("requirements");

    useEffect(() => {
        const updateLineCount = () => {
            if (_containerRef.current) {
                const containerHeight = _containerRef.current.clientHeight;
                const count = Math.floor(containerHeight / _lineHeight);
                setLineCount(count);
            }
        };

        window.addEventListener("resize", updateLineCount);
        updateLineCount();

        return () => {
            window.removeEventListener("resize", updateLineCount);
        };
    }, []);

    useEffect(() => {
        const updatedLogs = [];

        if (projectName)
            updatedLogs.push(`〉〉〉 프로젝트 이름: ${projectName}`);
        if (config) updatedLogs.push(`〉〉〉 Config 설정: ${config}`);
        if (requirements) updatedLogs.push(`〉〉〉 요구사항: ${requirements}`);

        setLogs(updatedLogs);
    }, [projectName, requirements, config]);

    const onSubmit = (data: any) => {
        setIsClickSubmit(true);
        reset();
        setLogs([]);
    };

    return (
        <ChatPresenterInput
            _lineHeight={_lineHeight}
            _lineCount={_lineCount}
            _containerRef={_containerRef}
            register={register}
            handleSubmit={handleSubmit}
            errors={errors}
            onSubmit={onSubmit}
            _isClickSubmit={_isClickSubmit}
            _logs={_logs}
        />
    );
}
