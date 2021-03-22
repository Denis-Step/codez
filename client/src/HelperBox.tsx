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
  InputLeftAddon,
} from "@chakra-ui/react";
import { BsBook } from "react-icons/bs";
import DefinitionModal from "./DefinitionModal";

const HelperBox = (): JSX.Element => {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [defModalOpen, setDefModalOpen] = useState(false);
  const [defModalWord, setDefModalWord] = useState<string>();
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
                <InputLeftAddon size="lg">
                  <Button
                    variant="solid"
                    leftIcon={<BsBook />}
                    onClick={(e) => setDefModalOpen(true)}
                  >
                    Get Definition
                  </Button>
                </InputLeftAddon>
                <DefinitionModal
                  isOpen={defModalOpen}
                  word={defModalWord}
                  closeModal={() => setDefModalOpen(false)}
                />
                <Input
                  variant="outline"
                  placeholder="Word"
                  onChange={(e) => setDefModalWord(e.target.value)}
                />
              </InputGroup>
            </DrawerBody>
          </DrawerContent>
        </DrawerOverlay>
      </Drawer>
    </Center>
  );
};

export default HelperBox;
