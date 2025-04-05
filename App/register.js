import { StyleSheet, Text, View, Image, TextInput, Pressable } from 'react-native';

export default function App() {
  return (
    <View style={styles.container}>

      <View>
        <Image source={{uri : "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/2052px-Pok%C3%A9_Ball_icon.svg.png"}} width={200} height={200}></Image>
      </View>

      <View>
        <Text style={styles.title}>Registrate</Text>
        <Text style={styles.label}>Nombre</Text>
        <TextInput style={styles.input}></TextInput>
        <Text style={styles.label}>Correo</Text>
        <TextInput style={styles.input}></TextInput>
        <Text style={styles.label}>Contraseña</Text>
        <TextInput style={styles.input}></TextInput>
        <Pressable style={styles.send}><Text>Enviar</Text></Pressable>
      </View>

      <View>
        <Text style={styles.containerFooter.texts}>Iniciar Sesión</Text>
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
  },

  containerFooter:{
    justifyContent: "center",
    alignItems: "center",
    texts:{
      fontSize: 20,
      margin: 5
    }
  }
});