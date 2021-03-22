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
  useDisclosure,
} from "@chakra-ui/react";
import { WordDefinition } from "./types/types";
import { get_Definition } from "./apicalls";

interface DefinitionModalProps {
  isOpen: boolean;
  closeModal: () => void;
  word: string | undefined;
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
        <li>{`${definition["word"]}: ${definition["definition"]}`}</li>
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
    } else {
      setDefinitions(undefined);
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
