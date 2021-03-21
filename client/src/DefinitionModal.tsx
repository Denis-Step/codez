import React, { useState, useEffect } from "react";
import {
  Button,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
  Spinner
} from "@chakra-ui/react";
import {WordDefinition} from "./types/types";

interface DefinitionModalProps {
    isOpen: boolean;
    closeModal: () => void;
}

const DefinitionModal = (props: DefinitionModalProps): JSX.Element => {
    const [definitions, setDefinitions] = useState<WordDefinition[]>();
  
  return (
    <>

      <Modal isOpen={props.isOpen} onClose={props.closeModal}>
        <ModalOverlay />
        <ModalContent>
          <ModalHeader>Definitions</ModalHeader>
          <ModalCloseButton />
          <ModalBody>
              {definitions || <Spinner />}
          </ModalBody>

          <ModalFooter>
            <Button colorScheme="pink" mr={3} onClick={props.closeModal}>
              Close
            </Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default DefinitionModal;