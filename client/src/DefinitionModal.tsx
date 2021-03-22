import React, { useState, useEffect, useMemo } from "react";
import {
  Button,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Spinner,
} from "@chakra-ui/react";
import { WordDefinition } from "./types/types";
import { get_Definition } from "./apicalls";

interface DefinitionModalProps {
  isOpen: boolean;
  closeModal: () => void;
  word: string | undefined;
}

function formatDef(word: string){
    const wordList = word.split(".");
    const formattedWord = `${wordList[0]} (${wordList[1]})`;
    return formattedWord;
}

const DefinitionModal = (props: DefinitionModalProps): JSX.Element => {
  const [definitions, setDefinitions] = useState<WordDefinition[]>();

  const DefinitionList = useMemo(() => {
    const defBoxes = [] as JSX.Element[];

    if (!definitions) {
      return <ol>{defBoxes}</ol>;
    }

    for (const definition of definitions) {
      const defBox = (
        <li>
            <em>{`${formatDef(definition["word"])}`}</em>: 
            {`${definition["definition"]}`}
        </li>
      );
      defBoxes.push(defBox);
    }

    return <ol>{defBoxes}</ol>;
  }, [definitions]);

  useEffect(() => {
    if (props.isOpen && props.word) {
      const getDefinitions = async (word: string) => {
        const defs = await get_Definition(word);
        setDefinitions(defs);
      };

      getDefinitions(props.word);
    }
  }, [props.word, props.isOpen]);

  return (
    <Modal isOpen={props.isOpen} onClose={props.closeModal}>
      <ModalOverlay />
      <ModalContent>
        <ModalHeader>Definitions</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          {definitions ? DefinitionList : <Spinner />}
        </ModalBody>

        <ModalFooter>
          <Button colorScheme="pink" mr={3} onClick={props.closeModal}>
            Close
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
};

export default DefinitionModal;
