import React, { useState } from 'react'
import Inputs, {Input} from './Inputs';

type FormProps = {
  title: string;
  buttonText: string;
  onSubmit: (data: any) => void;
  inputFields: Array<Input>;
  alternateLink: { prompt: string; text: string; url: string };
};


const Form: React.FC<FormProps> = ({
  title,
  buttonText,
  onSubmit,
  inputFields,
  alternateLink
  }) => {
    const [formData, setFormData] = useState<{ [key: string]: string}>({});
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
      setFormData({...formData, [e.target.name]: e.target.value});
    };
    const handleSubmit = (e: React.FormEvent) => {
      e.preventDefault();
      onSubmit(formData);
    };

  return (
    <>
      <form onSubmit={handleSubmit} className="p-4 bg-white space-y-4 text-center">
        <h2 className="text-2xl font-bold">{title}</h2>
        
        <Inputs onChange={handleChange} inputFields={inputFields} />
        
        <button type="submit" className="w-full py-2 mt-4 font-semibold text-white bg-blue-600 rounded-lg">
          {buttonText}
        </button>
        
        <p className="mt-4 text-center">
          {alternateLink.prompt}{' '}
          <a href={alternateLink.url} className="text-blue-600 hover:underline">
            {alternateLink.text}
          </a>
        </p>
      </form>
    </>
  )
}

export default Form