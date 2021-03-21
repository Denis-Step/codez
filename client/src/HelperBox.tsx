import React, { useRef, useState } from "react";
import {
  Button,
  Drawer,
  Center,
  DrawerBody,
  DrawerOverlay,
  DrawerContent,
  DrawerHeader,
  Input,
  InputGroup,
  useDisclosure,
  InputRightElement,
} from "@chakra-ui/react";
import { BsBook } from "react-icons/bs";
import DefinitionModal from "./DefinitionModal";

const HelperBox = (): JSX.Element => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [defModalOpen, setDefModalOpen] = useState(false);
  const btnRef = useRef<HTMLButtonElement>(null);

  return (
    <Center>
      <Button ref={btnRef} colorScheme="teal" onClick={onOpen}>
        Hints
      </Button>
      <Drawer placement={"bottom"} onClose={onClose} isOpen={isOpen}>
        <DrawerOverlay>
          <DrawerContent>
            <Center>
              <DrawerHeader borderBottomWidth="1px">
                SPYMASTER TOOLS
              </DrawerHeader>
            </Center>
            <DrawerBody>
              <InputGroup size="md">
                <DefinitionModal isOpen={defModalOpen} closeModal = {() => setDefModalOpen(false)} />
                <Input variant="outline" placeholder="Word" />
                <InputRightElement size="10rem">
                  <Button
                    variant="solid"
                    leftIcon={<BsBook />}
                    onClick={(e) => setDefModalOpen(true)}
                  >
                    Get Definition
                  </Button>
                </InputRightElement>
              </InputGroup>
            </DrawerBody>
          </DrawerContent>
        </DrawerOverlay>
      </Drawer>
    </Center>
  );
};

export default HelperBox;
