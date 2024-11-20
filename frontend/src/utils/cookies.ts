import { jwtDecode } from "jwt-decode";
import Cookies from "js-cookie";

export const setAccessToken = (token: string) => {
  const decodedToken: { exp: number } = jwtDecode(token);
  const expiresIn = decodedToken.exp * 1000 - Date.now();

  if (expiresIn > 0) {
    Cookies.set("accessToken", token, {
      expires: expiresIn / (1000 * 60 * 60 * 24), // Convert ms to days
      secure: true,
      sameSite: "Strict",
    });
    console.log(document.cookie);
  }
};

export const getAccessToken = (): string | null => {
  const match = document.cookie.match(new RegExp(`(^|; )accessToken=([^;]*)`));
  return match ? decodeURIComponent(match[2]) : null;
};

export const setRefreshToken = (token: string) => {
  const decodedToken: { exp: number } = jwtDecode(token);
  const expiresIn = decodedToken.exp * 1000 - Date.now();

  if (expiresIn > 0) {
    Cookies.set("refreshToken", token, {
      expires: expiresIn / (1000 * 60 * 60 * 24), // Convert ms to days
      secure: true,
      sameSite: "Strict",
    });
    console.log(document.cookie);
  }
};

export const getRefreshToken = (): string | null => {
  const match = document.cookie.match(new RegExp(`(^|; )refreshToken=([^;]*)`));
  return match ? decodeURIComponent(match[2]) : null;
};

export const deleteTokens = () => {
  document.cookie = "accessToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
  document.cookie = "refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
};
