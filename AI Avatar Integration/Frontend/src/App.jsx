import React from 'react';
import styled, { ThemeProvider } from 'styled-components';
import { motion } from 'framer-motion';
import GlobalStyle from './GlobalStyle';
import theme from './theme';
import ImageUpload from './ImageUpload';

const AppContainer = styled.div`
  text-align: center;
  background: ${({ theme }) => theme.colors.background};
  color: ${({ theme }) => theme.colors.text};
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
`;

const Heading = styled(motion.h1)`
  font-size: 3rem; /* Adjust this value to increase the heading size */
  margin: 20px 0;
  color: ${({ theme }) => theme.colors.primary};
`;

function App() {
  return (
    <ThemeProvider theme={theme}>
      <GlobalStyle />
      <AppContainer>
        <Heading initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ duration: 1 }}>
          Virtual Try-On
        </Heading>
        <ImageUpload />
      </AppContainer>
    </ThemeProvider>
  );
}

export default App;
