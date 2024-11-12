import React from 'react'

export type Input = { 
    type: string;
    name: string;
    placeholder: string;
};

interface InputsProps {
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
    inputFields: Array<Input>;
}


const Inputs: React.FC<InputsProps> = ({onChange, inputFields}) => {
  return (
    <>
        { inputFields.map((field) => (
            <input
                key={field.name}
                type={field.type}
                name={field.name}
                onChange={onChange}
                placeholder={field.placeholder}
                className="w-full px-4 py-2 border rounded-lg"
                required
            />
        )) }
    </>
  )
}

export default Inputs