<script>
	import { onMount } from 'svelte';
	let character;

	onMount(async () => {
		const response = await fetch('https://swapi.dev/api/people/1');
		const data = await response.json();
		character = data;
	});
</script>

<main>
	{#if character === undefined}
		Loading character...
	{:else}
		{character.name}
		<br />
		{character.mass}
	{/if}
</main>
