import 'package:flutter/material.dart';
class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ElevatedButton(
        onPressed: () {
          // Navigator.of(context).push(MaterialPageRoute(builder: (BuildCo))
        },
        child: const Text("Home Screen"),
        )
    );

  }
}
