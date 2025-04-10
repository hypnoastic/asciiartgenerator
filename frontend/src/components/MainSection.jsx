import React, { useState, useRef, useEffect } from 'react';
import "./MainSection.css"

const MainSection = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [outputImage, setOutputImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef(null);
  const previewURLRef = useRef(null);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;
    setSelectedFile(file);
    setOutputImage(null);
    if (previewURLRef.current) URL.revokeObjectURL(previewURLRef.current);
    previewURLRef.current = URL.createObjectURL(file);
  };

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleGenerate = async () => {
    if (!selectedFile) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('https://ascii-backend-52ls.onrender.com/upload/', {
        method: 'POST',
        body: formData,
      });

      const blob = await response.blob();
      const imageUrl = URL.createObjectURL(blob);
      setOutputImage(imageUrl);
    } catch (error) {
      console.error('Error:', error);
    }

    setLoading(false);
  };

  const handleDownload = () => {
    if (!outputImage) return;
    const a = document.createElement('a');
    a.href = outputImage;
    a.download = 'ascii_image.png';
    a.click();
  };

  useEffect(() => {
    return () => {
      if (previewURLRef.current) {
        URL.revokeObjectURL(previewURLRef.current);
      }
      if (outputImage) {
        URL.revokeObjectURL(outputImage);
      }
    };
  }, []);

  return (
      <main className="main-section">
        <div className="box-container">
          <div className="box upload-box">
            <input
                type="file"
                ref={fileInputRef}
                style={{ display: 'none' }}
                accept="image/*"
                onChange={handleFileChange}
            />
            {selectedFile && (
                <img
                    src={previewURLRef.current}
                    alt="Uploaded"
                    className="preview-img"
                />
            )}
            <button className="action-btn" onClick={handleUploadClick}>Upload</button>
          </div>

          <div className="box output-box">
            {loading ? (
                <div className="loader">Generating...</div>
            ) : (
                outputImage && (
                    <img
                        src={outputImage}
                        alt="Generated"
                        className="preview-img"
                    />
                )
            )}
            <button className="action-btn" onClick={handleDownload}>Download</button>
          </div>
        </div>

        <button className="generate-btn" onClick={handleGenerate}>Generate Photo</button>
      </main>
  );
};

export default MainSection;