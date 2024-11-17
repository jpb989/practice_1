export const setAccessToken = (token: string) => {
    document.cookie = `accessToken=${token}; path=/; HttpOnly; Secure; SameSite=Strict`;
};

export const getAccessToken = (): string | null => {
    const match = document.cookie.match(/(?:^|;)accessToken=([^;]*)/);
    return match ? match[1] : null;
};

export const setRefreshToken = (token: string) => {
    document.cookie = `refreshToken=${token}; path=/; HttpOnly; Secure; SameSite=Strict`;
};

export const getRefreshToken = (): string | null => {
    const match = document.cookie.match(/(?:^|;)refreshToken=([^;]*)/);
    return match ? match[1] : null;
};

export const deleteTokens = () => {
    document.cookie = 'accessToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
    document.cookie = 'refreshToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/';
};