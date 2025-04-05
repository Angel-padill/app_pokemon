import { StyleSheet, Text, View, TextInput, Pressable } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>

      <View>
        <Text style={styles.title}>Actualiza tu información</Text>
        <Text style={styles.label}>Edita tu nombre:</Text>
        <TextInput style={styles.input}></TextInput>
        <Text style={styles.label}>Edita tu correo:</Text>
        <TextInput style={styles.input}></TextInput>
        <Text style={styles.label}>Edita tu contraseña:</Text>
        <TextInput style={styles.input}></TextInput>
        <Pressable style={styles.send}><Text>Subir</Text></Pressable>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#fff',
    padding: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },

  title: {
    fontSize: 24,
    fontWeight: "bold"
  },

  label: {
    fontSize: 15,
    fontWeight: "bold"
  },

  input: {
    borderRadius: 10,
    borderWidth: 2,
    borderColor: "black",
    fontSize: 15,
    width: "auto"
  },

  send: {
    backgroundColor: "red",
    width: "auto",
    height: "auto",
    borderRadius: 10,
    marginTop: 15,
    alignItems: "center",
    textButton: {
      color:"black",
      fontSize: 20,
      fontWeight: "bold",
    }
  }
});