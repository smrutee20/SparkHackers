import React, { useState, useRef } from 'react';
import styled from 'styled-components';
import { motion } from 'framer-motion';
import submitImage from './image.png';

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 20px 0;
`;

const ButtonContainer = styled.div`
  display: flex;
  justify-content: center;
  gap: 50px;
  margin: 40px 40px;
`;

const ImageUploadButton = styled(motion.button)`
  width: 400px;
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid ${({ theme }) => theme.colors.primary};
  background: ${({ theme }) => theme.colors.primary};
  color: white;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
  text-align: center;

  &:hover {
    background: ${({ theme }) => theme.colors.secondary};
    border-color: ${({ theme }) => theme.colors.secondary};
  }
`;

const ImagePreview = styled.img`
  max-width: 100%;
  height: auto;
  margin-top: 20px;
`;

const HiddenInput = styled.input`
  display: none;
`;

const SubmitButton = styled(motion.button)`
  width: 200px;
  height: 50px;
  margin-top: 20px;
  border: 2px solid ${({ theme }) => theme.colors.primary};
  background: ${({ theme }) => theme.colors.primary};
  color: white;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
  text-align: center;

  &:hover {
    background: ${({ theme }) => theme.colors.secondary};
    border-color: ${({ theme }) => theme.colors.secondary};
  }
`;

const ImageUpload = () => {
  const [personImage, setPersonImage] = useState(null);
  const [clothesImage, setClothesImage] = useState(null);
  const [flag , setFlag] = useState(false);


  const personInputRef = useRef(null);
  const clothesInputRef = useRef(null);

  const handlePersonClick = () => {
    personInputRef.current.click();
  };

  const handleClothesClick = () => {
    clothesInputRef.current.click();
  };

  const handleImageChange = (event, setImage) => {
    const file = event.target.files[0];
    if (file) {
      setImage(URL.createObjectURL(file));
    }
    setFlag(false);	
  };

  const handleSubmit = () => {
    // Add your submit logic here
    setFlag(true);
    console.log("Person Image:", personImage);
    console.log("Clothes Image:", clothesImage);
  };

  return (
    <Container>
      <ButtonContainer>
        <ImageUploadButton whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} onClick={handlePersonClick}>
          Upload Person Image
        </ImageUploadButton>
        <HiddenInput
          ref={personInputRef}
          type="file"
          accept="image/*"
          onChange={(event) => handleImageChange(event, setPersonImage)}
        />
        
        <ImageUploadButton whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} onClick={handleClothesClick}>
          Upload Clothes Image
        </ImageUploadButton>
        <HiddenInput
          ref={clothesInputRef}
          type="file"
          accept="image/*"
          onChange={(event) => handleImageChange(event, setClothesImage)}
        />
      </ButtonContainer>

      {personImage && <ImagePreview src={personImage} alt="Person" />}
      {clothesImage && <ImagePreview src={clothesImage} alt="Clothes" />}
	{flag && <ImagePreview src={submitImage} alt="Try-On"/>}
      <SubmitButton whileHover={{ scale: 1.1 }} whileTap={{ scale: 0.9 }} onClick={handleSubmit}>
        Submit
      </SubmitButton>
    </Container>
  );
};

export default ImageUpload;
