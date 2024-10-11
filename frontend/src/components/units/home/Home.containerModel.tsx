import { useRef, useState } from "react";
import * as THREE from "three";
import { useGLTF } from "@react-three/drei";
import { useFrame } from "@react-three/fiber";

import HomePresenterModel from "./Home.presenterModel";
import { IHomeContainerModel } from "./Home.types";

export default function HomeContainerModel(props: IHomeContainerModel) {
    const _group = useRef<any>();
    const [_isClickedLogin, setIsClickedLogin] = useState<Boolean>(false);
    const { nodes, materials } = useGLTF("/3d/mac.glb");
    const _pressedColor = new THREE.Color("red");
    const _keyboardKeys = [
        "keyboard1",
        "keyboard2",
        "keyboard3",
        "keyboard4",
        "keyboard5",
        "keyboard6",
        "keyboard7",
        "keyboard8",
        "keyboard9",
        "keyboard0",
        "keyboardQ",
        "keyboardW",
        "keyboardE",
        "keyboardR",
        "keyboardT",
        "keyboardY",
        "keyboardU",
        "keyboardI",
        "keyboardO",
        "keyboardP",
        "keyboardA",
        "keyboardS",
        "keyboardD",
        "keyboardF",
        "keyboardG",
        "keyboardH",
        "keyboardJ",
        "keyboardK",
        "keyboardL",
        "keyboardZ",
        "keyboardX",
        "keyboardC",
        "keyboardV",
        "keyboardB",
        "keyboardN",
        "keyboardM",
    ];

    const onChangeIsClickedLogin = () => {
        setIsClickedLogin(!_isClickedLogin);
    };

    useFrame((state) => {
        if (!_isClickedLogin) {
            const t = state.clock.getElapsedTime();

            _group.current.rotation.x = THREE.MathUtils.lerp(
                _group.current.rotation.x,
                Math.cos(t / 2) / 20 + 0.25,
                0.1
            );

            _group.current.rotation.y = THREE.MathUtils.lerp(
                _group.current.rotation.y,
                Math.sin(t / 4) / 20,
                0.1
            );

            _group.current.rotation.z = THREE.MathUtils.lerp(
                _group.current.rotation.z,
                Math.sin(t / 8) / 20,
                0.1
            );

            _group.current.position.y = THREE.MathUtils.lerp(
                _group.current.position.y,
                (-2 + Math.sin(t / 2)) / 2,
                0.1
            );
        } else {
            _group.current.rotation.set(0.3, 0, 0);
            _group.current.position.set(0, -2.5, 0);

            const currentScale = _group.current.scale.x;
            const targetScale = 1.4;
            _group.current.scale.setScalar(
                THREE.MathUtils.lerp(currentScale, targetScale, 0.02)
            );
        }
    });

    return (
        <>
            <HomePresenterModel
                _pressedKey={props._pressedKey}
                _group={_group}
                nodes={nodes}
                materials={materials}
                _keyboardKeys={_keyboardKeys}
                _pressedColor={_pressedColor}
                _isClickedLogin={_isClickedLogin}
                onChangeIsClickedLogin={onChangeIsClickedLogin}
            />
        </>
    );
}
