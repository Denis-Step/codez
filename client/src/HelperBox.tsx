import React, { useRef } from "react";
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

const HelperBox = (): JSX.Element => {
  const { isOpen, onOpen, onClose } = useDisclosure();
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
                <Input variant="outline" placeholder="Word" />
                <InputRightElement size="10rem">
                  <Button variant="solid" leftIcon={<BsBook />}>Get Definition</Button>
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
