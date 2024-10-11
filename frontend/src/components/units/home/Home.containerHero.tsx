"use client";

import { Suspense, useRef } from "react";
import Router from "next/router";
import * as THREE from "three";
import { useGLTF } from "@react-three/drei";
import { Canvas, useFrame } from "@react-three/fiber";

import HomePresenterHero from "./Home.presenterHero";
import { IHomeContainerHero } from "./Home.types";
import { GET_KAKAO_OAUTH_URI } from "./Home.queries";

export default function HomeContainerHero(props: IHomeContainerHero) {
    const router = Router;

    const KakaoModel = () => {
        const _kakaoGroup = useRef<any>();
        const { scene } = useGLTF("/3d/kakao.glb");

        const handleClickKakao = (event: any) => {
            event.stopPropagation();
            GET_KAKAO_OAUTH_URI();
            router.push("/chat");
        };

        const handlePointerOverKakao = () => {
            document.body.style.cursor = "pointer";
        };

        const handlePointerOutKakao = () => {
            document.body.style.cursor = "default";
        };

        useFrame((state) => {
            const t = state.clock.getElapsedTime();

            _kakaoGroup.current.rotation.x = THREE.MathUtils.lerp(
                _kakaoGroup.current.rotation.x,
                Math.cos(t / 2) / 20 + 0.25,
                0.1
            );

            _kakaoGroup.current.rotation.y = THREE.MathUtils.lerp(
                _kakaoGroup.current.rotation.y,
                Math.sin(t / 4) / 20,
                0.1
            );

            _kakaoGroup.current.position.y = THREE.MathUtils.lerp(
                _kakaoGroup.current.position.y,
                (3 + Math.sin(t / 2)) / 2,
                0.1
            );
        });

        return (
            <group
                ref={_kakaoGroup}
                position={[-5, 0, 0]}
                scale={0.2}
                onPointerDown={handleClickKakao}
                onPointerOver={handlePointerOverKakao}
                onPointerOut={handlePointerOutKakao}
            >
                <primitive object={scene} />
            </group>
        );
    };

    const Kakao = () => {
        return (
            <Suspense fallback={null}>
                <KakaoModel />
                <pointLight position={[-5, 1.5, 0]} intensity={1.5} />
            </Suspense>
        );
    };

    const GoogleModel = () => {
        const _googleGroup = useRef<any>();
        const { scene } = useGLTF("/3d/google.glb");

        const handleClickGoogle = (event: any) => {
            event.stopPropagation();
            alert("Google Model Clicked!");
            router.push("/chat");
        };

        const handlePointerOverGoogle = () => {
            document.body.style.cursor = "pointer";
        };

        const handlePointerOutGoogle = () => {
            document.body.style.cursor = "default";
        };

        useFrame((state) => {
            const t = state.clock.getElapsedTime();

            _googleGroup.current.rotation.x = THREE.MathUtils.lerp(
                _googleGroup.current.rotation.x,
                Math.cos(t / 2) / 20 + 0.25,
                0.1
            );

            _googleGroup.current.rotation.y = THREE.MathUtils.lerp(
                _googleGroup.current.rotation.y,
                Math.sin(t / 4) / 20,
                0.1
            );

            _googleGroup.current.position.y = THREE.MathUtils.lerp(
                _googleGroup.current.position.y,
                (2.8 + Math.sin(t / 2)) / 2,
                0.1
            );
        });

        return (
            <group
                ref={_googleGroup}
                position={[-2.85, 0, 0]}
                scale={0.7}
                onPointerDown={handleClickGoogle}
                onPointerOver={handlePointerOverGoogle}
                onPointerOut={handlePointerOutGoogle}
            >
                <primitive object={scene} />
            </group>
        );
    };

    const Google = () => {
        return (
            <Suspense fallback={null}>
                <GoogleModel />
                <pointLight position={[-2.5, 1.5, 0]} intensity={1.5} />
            </Suspense>
        );
    };

    const GitModel = () => {
        const _gitGroup = useRef<any>();
        const { scene } = useGLTF("/3d/git.glb");

        const handleClickGit = (event: any) => {
            event.stopPropagation();
            alert("Git Model Clicked!");
            router.push("/chat");
        };

        const handlePointerOverGit = () => {
            document.body.style.cursor = "pointer";
        };

        const handlePointerOutGit = () => {
            document.body.style.cursor = "default";
        };

        useFrame((state) => {
            const t = state.clock.getElapsedTime();

            _gitGroup.current.rotation.x = THREE.MathUtils.lerp(
                _gitGroup.current.rotation.x,
                Math.cos(t / 2) / 20 + 0.25,
                0.1
            );

            _gitGroup.current.rotation.y = THREE.MathUtils.lerp(
                _gitGroup.current.rotation.y,
                Math.sin(t / 4) / 20,
                0.1
            );

            _gitGroup.current.position.y = THREE.MathUtils.lerp(
                _gitGroup.current.position.y,
                (2.8 + Math.sin(t / 2)) / 2,
                0.1
            );
        });

        return (
            <group
                ref={_gitGroup}
                position={[-0.8, 0, 0]}
                scale={0.7}
                onPointerDown={handleClickGit}
                onPointerOver={handlePointerOverGit}
                onPointerOut={handlePointerOutGit}
            >
                <primitive object={scene} />
            </group>
        );
    };

    const Git = () => {
        return (
            <Suspense fallback={null}>
                <GitModel />
                <pointLight position={[-0.5, 1.5, 0]} intensity={1.5} />
            </Suspense>
        );
    };

    const IconBox = () => {
        return (
            <Canvas>
                <Suspense fallback={null}>
                    <Kakao />
                    <Google />
                    <Git />
                    <ambientLight intensity={3} />
                </Suspense>
            </Canvas>
        );
    };

    return (
        <>
            <HomePresenterHero
                _isClickedLogin={props._isClickedLogin}
                onChangeIsClickedLogin={props.onChangeIsClickedLogin}
                IconBox={<IconBox />}
            />
        </>
    );
}
