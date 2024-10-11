import * as THREE from "three";
import { Html } from "@react-three/drei";

import HomeContainerHero from "./Home.containerHero";
import * as S from "./Home.styles";
import { IHomePresenterModel } from "./Home.types";

export default function HomePresenterModel(props: IHomePresenterModel) {
    return (
        <>
            <group ref={props._group} dispose={null}>
                <group rotation-x={-0.425} position={[0, -0.04, 0.41]}>
                    <group
                        position={[0, 2.96, -0.13]}
                        rotation={[Math.PI / 2, 0, 0]}
                    >
                        <mesh
                            material={props.materials.aluminium}
                            geometry={props.nodes["Cube008"].geometry}
                        />
                        <mesh
                            material={props.materials["matte.001"]}
                            geometry={props.nodes["Cube008_1"].geometry}
                        />
                        <mesh geometry={props.nodes["Cube008_2"].geometry}>
                            <Html
                                rotation-x={-Math.PI / 2}
                                position={[0, 0.05, -0.09]}
                                transform
                                occlude
                            >
                                <S.HomePresenterHeroWrapper
                                    onPointerDown={(e) => e.stopPropagation()}
                                >
                                    <HomeContainerHero
                                        _isClickedLogin={props._isClickedLogin}
                                        onChangeIsClickedLogin={
                                            props.onChangeIsClickedLogin
                                        }
                                    />
                                </S.HomePresenterHeroWrapper>
                            </Html>
                        </mesh>
                    </group>
                </group>
                <mesh
                    material={props.materials.keys}
                    geometry={props.nodes.keyboard.geometry}
                    position={[1.79, 0, 3.45]}
                />
                {props._keyboardKeys.map((el) => (
                    <mesh
                        key={el}
                        geometry={props.nodes[el].geometry}
                        position={[1.79, 0, 3.45]}
                        material={
                            props._pressedKey === el
                                ? new THREE.MeshStandardMaterial({
                                      color: props._pressedColor,
                                  })
                                : props.materials.keys
                        }
                    />
                ))}
                <group position={[0, -0.1, 3.39]}>
                    <mesh
                        material={props.materials.aluminium}
                        geometry={props.nodes["Cube002"].geometry}
                    />
                    <mesh
                        material={props.materials.trackpad}
                        geometry={props.nodes["Cube002_1"].geometry}
                    />
                </group>
                <mesh
                    material={props.materials.touchbar}
                    geometry={props.nodes.touchbar.geometry}
                    position={[0, -0.03, 1.2]}
                />
            </group>
        </>
    );
}
