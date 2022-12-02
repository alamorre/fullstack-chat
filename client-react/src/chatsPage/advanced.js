import {
  useMultiChatLogic,
  MultiChatSocket,
  MultiChatWindow,
} from "react-chat-engine-advanced";

const ChatsPage = (props) => {
  const chatProps = useMultiChatLogic(
    process.env.REACT_APP_CHAT_ENGINE_PROJECT_ID,
    props.user.username,
    props.user.secret
  );

  return (
    <div style={{ height: "100vh" }}>
      <MultiChatSocket {...chatProps} />

      <MultiChatWindow {...chatProps} style={{ height: "100%" }} />
    </div>
  );
};

export default ChatsPage;
